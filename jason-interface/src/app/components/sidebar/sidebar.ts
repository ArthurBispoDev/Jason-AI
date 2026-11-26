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

  chats: ChatModel[] = this.chatService.chats();


}
