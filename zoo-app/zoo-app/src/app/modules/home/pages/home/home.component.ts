import {Component, OnInit} from '@angular/core';
import {Faq} from '../../../../shared/interfaces/faq.interface';
import {ApiService} from '../../../../core/services/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit{

  aboutUsText = null;
  faqs: Faq[] = [];

  constructor(private apiService: ApiService) { }

  public ngOnInit(): void {
    this.apiService.getAboutUsText().subscribe(aboutUsText => {
      this.aboutUsText = aboutUsText[0].description
    });
    this.apiService.getFAQs().subscribe(faqs => this.faqs = faqs);
  }
}
