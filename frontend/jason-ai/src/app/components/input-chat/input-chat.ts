import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [FormsModule],
  selector: 'app-input-chat',
  styleUrl: './input-chat.scss',
  templateUrl: './input-chat.html',
})
export class InputChat {

  mensagem: string = '';

  enviarMensagem() {
    console.log(this.mensagem);

    this.mensagem = '';
  }
}
