import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ROUTER_NAMES} from "./core/constants/router-names";
import {HomeComponent} from "./modules/home/pages/home/home.component";
import {CatalogComponent} from "./modules/catalog/pages/catalog/catalog.component";
import {ItemComponent} from "./modules/catalog/pages/item/item.component";

const routes: Routes = [
  {
    path: ROUTER_NAMES.HOME,
    component: HomeComponent
  },
  {
    path: ROUTER_NAMES.BIO_ZONES,
    component: CatalogComponent,
    pathMatch: 'full'
  },
  {
    path: ROUTER_NAMES.ANIMALS,
    component: CatalogComponent,
    pathMatch: "full"
  },
  {
    path: ROUTER_NAMES.ANIMALS_TYPES,
    component: CatalogComponent,
    pathMatch: 'full'
  },
  {
    path: ROUTER_NAMES.ANIMAL,
    component: ItemComponent,
    pathMatch: "full"
  },
  {
    path: ROUTER_NAMES.EMPLOYEES,
    component: CatalogComponent,
    pathMatch: "full"
  },
  {
    path: ROUTER_NAMES.EMPLOYEE,
    component: ItemComponent,
    pathMatch: "full"
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
