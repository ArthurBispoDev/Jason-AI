import { Injectable, signal } from '@angular/core';
import { ChatModel } from '../models/chat.model';

@Injectable({
    providedIn: 'root'
})
export class ChatService {

    chats = signal<ChatModel[]>([
        {
            nome: 'Estudando Java',
            id: 19
        },
        {
            nome: 'Bom dia Jason',
            id: 2
        }
    ]);

    conversaAtualId = signal<number | null>(null);

}