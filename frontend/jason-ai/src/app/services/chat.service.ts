import { inject, Injectable, signal } from '@angular/core';
import { ChatModel } from '../models/chat.model';
import { Router } from '@angular/router';
import { MessageModel } from '../models/message.model';

@Injectable({
    providedIn: 'root'
})
export class ChatService {

    private router = inject(Router);

    chats = signal<ChatModel[]>([
        {
            nome: 'Estudando Java',
            id: 1
        },
        {
            nome: 'Bom dia Jason',
            id: 2
        },
        {
            nome: 'Sistema funcionando?',
            id: 3
        },
        {
            nome: 'Qual placa de vídeo...',
            id: 4
        },
        {
            nome: 'Projeto de Sistema Cozz',
            id: 5
        },
        
    ]);

    conversaAtualId = signal<number | null>(null);

    messages = signal<MessageModel[]>([]);

    mudaConversa(chatId: number | null) {
        this.conversaAtualId.set(
        chatId
        );

        this.messages.set(this.buscaMensagensPorChat(chatId));
        console.log(this.messages())

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
}