import { inject, Injectable, signal } from '@angular/core';
import { ChatModel, MessagesChatResponse } from '../models/chat.model';
import { Router } from '@angular/router';
import { MessageModel } from '../models/message.model';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

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

    enviarMensagemUser(content: string) {
        if (this.conversaAtualId() === null) return;

        const newMessage: MessageModel = {
            id: -1,
            role: 'user',
            content: content,
            createdAt: new Date()
        }

        this.messages.update(lista => [...lista, newMessage]);

        return newMessage;
    }

    mudaConversa(chatId: number | null) {
        this.conversaAtualId.set(
        chatId
        );

        this.router.navigate(['/c', chatId]);
    }

    atualizarMenssagensBanco(conversationId: number): void {
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