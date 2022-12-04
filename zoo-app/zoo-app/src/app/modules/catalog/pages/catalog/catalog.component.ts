import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { DisplayItem } from "../../../../shared/interfaces/display-item.interface";
import {ROUTER_NAMES} from '../../../../core/constants/router-names';
import {ApiService} from "../../../../core/services/api.service";

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.scss']
})
export class CatalogComponent implements OnInit {
  public pageTitle!: string;
  public buttonText!: string;
  public displayList!: DisplayItem[];

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
    switch (this.route.snapshot.routeConfig?.path) {
      case ROUTER_NAMES.BIO_ZONES : {
        this.apiService.getCountries().subscribe(countries => {
          this.pageTitle = 'Каталог био зон';
          this.displayList = countries;
          this.buttonText = 'Просмотреть всех';
        });
        break;
      }
      case ROUTER_NAMES.ANIMALS_TYPES : {
        this.apiService.getCategories(this.route.snapshot.params['country']).subscribe(categories => {
          this.pageTitle = 'Каталог типов зверей';
          this.displayList = categories;
          this.buttonText = 'Просмотреть всех';
        });
        break;
      }
      case ROUTER_NAMES.ANIMALS : {
        this.apiService.getAnimals(this.route.snapshot.params['category']).subscribe(animals => {
            this.pageTitle = 'Каталог зверей';
            this.displayList = animals;
            this.buttonText = 'Подробней';
          });
        break;
      }
      case ROUTER_NAMES.EMPLOYEES: {
        this.apiService.getEmployees().subscribe(employees => {
          this.pageTitle = 'Список сотрудников';
          this.displayList = employees;
          this.buttonText = 'Подробней';
        });
        break;
      }
    }
  }
}
