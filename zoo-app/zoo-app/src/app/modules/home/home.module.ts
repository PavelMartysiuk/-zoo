import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './pages/home/home.component';
import { CarouselComponent } from './components/carousel/carousel.component';
import { FaqComponent } from './components/faq/faq.component';
import { AboutUsComponent } from './components/about-us/about-us.component';



@NgModule({
  declarations: [
    HomeComponent,
    CarouselComponent,
    FaqComponent,
    AboutUsComponent
  ],
  imports: [
    CommonModule
  ]
})
export class HomeModule { }
