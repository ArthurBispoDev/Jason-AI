import { Component, inject, signal } from '@angular/core';
import { ChatModel } from '../../models/chat.model';
import { ChatService } from '../../services/chat.service';
import { Chat } from '../../pages/chat/chat';

@Component({
  imports: [],
  selector: 'app-sidebar',
  styleUrl: './sidebar.scss',
  templateUrl: './sidebar.html',
})
export class Sidebar {

    private chatService = inject(ChatService);

    chats = this.chatService.conversas;

    ngOnInit(): void {
        this.chatService.atualizarConversasBanco();
    }

    mudaConversa(chatId: number) {
        this.chatService.mudaConversa(chatId);
        this.chatService.atualizarMenssagensBanco(chatId);
    }
}
