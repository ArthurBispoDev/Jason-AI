import { inject, Injectable, signal } from '@angular/core';
import { ChatModel, JasonResponse, MessagesChatResponse } from '../models/chat.model';
import { Router } from '@angular/router';
import { MessageModel } from '../models/message.model';
import { HttpClient } from '@angular/common/http';
import { Observable, firstValueFrom } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class ChatService {

    private router = inject(Router);
    private http = inject(HttpClient);

    private readonly API_URL = 'http://127.0.0.1:8000/conversations';

    conversaAtualId = signal<number | null>(null);

    messages = signal<MessageModel[]>([]);
    conversas = signal<ChatModel[]>([]);

    async enviarMensagemUser(content: string) {
        if(this.conversaAtualId() === null) return null;

        const existsConversa: boolean = this.conversas().some(
            (conversa) => conversa.id === this.conversaAtualId()
        );

        this.messages.update((listaAtual) => [...listaAtual, {
            id: -1,
            role: 'user',
            content: content,
            createdAt: new Date()
        }]);

        if(!existsConversa) return null; // A fazer ainda

        this.messages.update((listaAtual) => [...listaAtual, {
            id: -2,
            role: 'assistant',
            content: 'Processando...',
            createdAt: new Date()
        }]);

        try {
             await firstValueFrom(
                this.http.post<JasonResponse>(
                    `${this.API_URL}/${this.conversaAtualId()}/messages`, 
                    { content }
                )
            );

            this.atualizarMenssagensBanco(this.conversaAtualId());

        } catch (erro) {
            this.atualizarMenssagensBanco(this.conversaAtualId());

            this.messages.update((listaAtual) => [...listaAtual, {
                id: -1,
                role: 'assistant',
                content: 'Falha ao processar mensagem. Tente novamente',
                createdAt: new Date()
            }]);
        }

        return null;
    }

    mudaConversa(chatId: number | null) {
        this.conversaAtualId.set(
        chatId
        );

        this.router.navigate(['/c', chatId]);
    }

    atualizarMenssagensBanco(conversationId: number | null): void {
        if(conversationId === null) return;

        this.getMessages(conversationId).subscribe({
            next: (response) => {
                this.messages.set(response.messages);
            },
            error: (error) => {
                console.error('Erro ao carregar mensagens:', error);
            }
        });
    }

    atualizarConversasBanco() {
        this.getConversations().subscribe({
            next: (response) => {
                this.conversas.set(response);
            },
            error: (error) => {
                console.log('Erro ao carregar conversas: ', error);
            }

        });
    }

    private getMessages(conversationId: number): Observable<MessagesChatResponse> {
        return this.http.get<MessagesChatResponse>(
            `${this.API_URL}/${conversationId}`
        );
    }

    private getConversations(): Observable<ChatModel[]> {
        return this.http.get<ChatModel[]>(this.API_URL);
    }
}