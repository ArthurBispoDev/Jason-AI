import { Routes } from '@angular/router';
import { Chat } from './pages/chat/chat';

export const routes: Routes = [
    {
        path: 'c',
        component: Chat
    },
    {
        path: 'c/:id',
        component: Chat
    }
];
