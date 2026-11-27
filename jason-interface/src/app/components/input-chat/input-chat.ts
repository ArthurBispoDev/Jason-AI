import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChatService } from '../../services/chat.service';

@Component({
  imports: [FormsModule],
  selector: 'app-input-chat',
  styleUrl: './input-chat.scss',
  templateUrl: './input-chat.html',
})
export class InputChat {
  private chatService = inject(ChatService);

  mensagem: string = '';

  enviarMensagem() {
    if(!this.mensagem.trim()) return;

    console.log(this.chatService.enviarMensagemUser(this.mensagem.trim()));

    this.mensagem = '';
  }
}
