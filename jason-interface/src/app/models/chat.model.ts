import { MessageModel } from "./message.model";

export interface ChatModel {
    id: number;
    title: string;
    nome: string;
};

export interface MessagesChatResponse {
    id: number;
    title: string;
    created_at: Date;
    messages: MessageModel[];
}