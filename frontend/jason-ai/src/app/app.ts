import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  imports: [RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.scss',
  templateUrl: './app.html',
})
export class App {
  splitStatus = {
    'Conversas': true,
    'Configurações': false
  };

  protected readonly title = signal('jason-ai');
}
