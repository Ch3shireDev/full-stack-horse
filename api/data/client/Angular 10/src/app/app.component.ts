import { AppService } from './app.service';
import { Message } from './message';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'client';
  messages: Message[];
  content: string;
  constructor(private appService: AppService) { }

  ngOnInit(): void {
    this.refresh();
  }

  refresh(): void {
    this.appService.getMessages().subscribe((messages: Message[]) => { this.messages = messages; });
  }

  submit(): void {
    if (this.content === undefined) { return; }
    const message = new Message();
    message.content = this.content;
    this.appService.postMessage(message).subscribe(res => { this.refresh(); });
  }
}
