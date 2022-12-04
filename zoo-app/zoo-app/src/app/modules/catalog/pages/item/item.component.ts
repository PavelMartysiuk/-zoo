import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Animal} from "../../../../shared/interfaces/animal.interface";
import {Employee} from "../../../../shared/interfaces/employee.interface";
import {ROUTER_NAMES} from '../../../../core/constants/router-names';
import {ApiService} from "../../../../core/services/api.service";

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.scss']
})
export class ItemComponent implements OnInit{
  animal!: Animal;
  employee!: Employee;
  itemType!: 'beast' | 'employee';

  constructor(
    private route: ActivatedRoute,
    private apiServices: ApiService
    ) {  }

  ngOnInit(): void {
    switch (this.route.snapshot.routeConfig?.path) {
      case ROUTER_NAMES.ANIMAL : {
        this.apiServices.getCurrentAnimal(this.route.snapshot.params['beastId']).subscribe(beast => {
          this.itemType = "beast";
          this.animal = beast;
        });
        break;
      }
      case ROUTER_NAMES.EMPLOYEE : {
        this.apiServices.getCurrentEmployee(this.route.snapshot.params['employeeId']).subscribe(employee => {
          this.itemType = "employee";
          this.employee = employee;
        });
        break;
      }
    }
  }
}
