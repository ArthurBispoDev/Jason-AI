export interface MessageModel {
    id: number;
    role: 'user' | 'assistant';
    content: string;
    createdAt: Date;
};