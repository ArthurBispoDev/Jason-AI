import { Component, inject, signal } from '@angular/core';
import { ChatModel } from '../../models/chat.model';
import { ChatService } from '../../services/chat.service';

@Component({
  imports: [],
  selector: 'app-sidebar',
  styleUrl: './sidebar.scss',
  templateUrl: './sidebar.html',
})
export class Sidebar {

  private chatService = inject(ChatService);

  chats = signal<ChatModel[]>([]);

  ngOnInit(): void {
        this.chatService.getConversations().subscribe({
            next: (data) => {
                this.chats.set(data);
            },
            error: (error) => {
                console.error('Erro ao buscar conversas:', error);
            }
        });
    }

    mudaConversa(chatId: number) {
        this.chatService.mudaConversa(chatId);
        this.chatService.mudaConversa(chatId);
        this.chatService.loadMessages(chatId);
    }
}
