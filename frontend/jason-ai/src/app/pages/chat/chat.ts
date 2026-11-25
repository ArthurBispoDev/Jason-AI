import { Component, inject, signal } from '@angular/core';
import { Sidebar } from '../../components/sidebar/sidebar';
import { ActivatedRoute } from '@angular/router';
import { ChatService } from '../../services/chat.service';

@Component({
  imports: [Sidebar],
  selector: 'app-chat',
  styleUrl: './chat.scss',
  templateUrl: './chat.html',
})
export class Chat {
  private route = inject(ActivatedRoute);
  private chatService = inject(ChatService);

  ngOnInit() {
    this.mudaConversa(Number(this.route.snapshot.paramMap.get('id')))
  }
  
  mudaConversa(id: number | null) {
    this.chatService.conversaAtualId.set(
      id
    );

    this.router.navigate(['/configuracoes']);

  }

  
}
