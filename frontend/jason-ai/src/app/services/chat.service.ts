import { inject, Injectable, signal } from '@angular/core';
import { ChatModel } from '../models/chat.model';
import { Router } from '@angular/router';

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

    mudaConversa(id: number | null) {
    this.conversaAtualId.set(
      id
    );

    this.router.navigate(['/c', id]);
  }

}