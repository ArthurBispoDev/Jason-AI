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
    private _messages = signal<MessageModel[]>([]);

    conversaAtualId = signal<number | null>(null);

    messages = this._messages.asReadonly();

    mudaConversa(chatId: number | null) {
        this.conversaAtualId.set(
        chatId
        );

        this.router.navigate(['/c', chatId]);
    }

    private buscaMensagensPorChat(chatId: number | null): MessageModel[] {
        if (chatId === null) return [];

        const data: Record<number, MessageModel[]> = {
            1: [
                {
                    id: 10,
                    role: 'user',
                    content: 'Olá Jason, como você está',
                    createdAt: new Date()
                },
                {
                    id: 11,
                    role: 'assistant',
                    content: 'Estou bem, Senhor. Obrigado por perguntar!',
                    createdAt: new Date()
                }
            ]
        };

        return data[chatId] ?? [];
    }

    getConversations(): Observable<ChatModel[]> {
        return this.http.get<ChatModel[]>(this.API_URL);
    }

    loadMessages(conversationId: number): void {
        this.getMessages(conversationId).subscribe({
            next: (response) => {
                this._messages.set(response.messages);
            },
            error: (error) => {
                console.error('Erro ao carregar mensagens:', error);
            }
        });
    }

    private getMessages(conversationId: number): Observable<MessagesChatResponse> {
        return this.http.get<MessagesChatResponse>(
            `${this.API_URL}/${conversationId}`
        );
    }
}