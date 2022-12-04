import {Component, Input} from '@angular/core';
import {Faq} from "../../../../shared/interfaces/faq.interface";

@Component({
  selector: 'app-faq',
  templateUrl: './faq.component.html',
  styleUrls: ['./faq.component.scss']
})
export class FaqComponent {

  @Input() faqs: Faq[] = [];

  constructor() { }
}
