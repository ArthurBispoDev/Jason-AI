import { Component, inject, signal, OnInit } from '@angular/core';
import { Sidebar } from '../../components/sidebar/sidebar';
import { ActivatedRoute } from '@angular/router';
import { ChatService } from '../../services/chat.service';
import { InputChat } from '../../components/input-chat/input-chat';
import { MessageModel } from '../../models/message.model';

@Component({
  imports: [Sidebar, InputChat],
  selector: 'app-chat',
  styleUrl: './chat.scss',
  templateUrl: './chat.html',
})
export class Chat implements OnInit {

  private route = inject(ActivatedRoute);
  private chatService = inject(ChatService);

  idUri = signal<number>(Number(this.route.snapshot.paramMap.get('id')));
  messages = signal<MessageModel[]>([]);

  ngOnInit() {
    if (this.idUri() !== 0) {
        this.chatService.mudaConversa(this.idUri());
        this.chatService.atualizarMenssagensBanco(this.idUri());
    }
  }
}