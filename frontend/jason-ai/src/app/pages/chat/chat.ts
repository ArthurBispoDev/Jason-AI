import { Component, inject, signal } from '@angular/core';
import { Sidebar } from '../../components/sidebar/sidebar';
import { ActivatedRoute } from '@angular/router';
import { ChatService } from '../../services/chat.service';
import { InputChat } from '../../components/input-chat/input-chat';

@Component({
  imports: [Sidebar, InputChat],
  selector: 'app-chat',
  styleUrl: './chat.scss',
  templateUrl: './chat.html',
})
export class Chat {
  private route = inject(ActivatedRoute);
  private chatService = inject(ChatService);

  idUri = signal<number>(Number(this.route.snapshot.paramMap.get('id')));

  ngOnInit() {

    if (this.idUri() !== 0) {
      this.chatService.mudaConversa(this.idUri());
    }
  
  }
  
}
