import { Injectable } from '@angular/core';
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {DisplayItem} from "../../shared/interfaces/display-item.interface";
import {Animal} from "../../shared/interfaces/animal.interface";
import {Employee} from "../../shared/interfaces/employee.interface";
import {Faq} from "../../shared/interfaces/faq.interface";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private readonly apiEndpoint = environment.apiEndpoint;

  constructor(private http: HttpClient) { }

   public getAboutUsText(): Observable<any> {
    return this.http.get(this.apiEndpoint + '/about');
   }

   public getAnimals(category: string): Observable<DisplayItem[]> {
    return this.http.get<DisplayItem[]>(this.apiEndpoint + `/animal/?category=${category}`);
   }

   public getCurrentAnimal(id: number): Observable<Animal> {
    return this.http.get<Animal>(this.apiEndpoint + `/animal/${id}`);
   }

   public getCategories(country: string): Observable<DisplayItem[]> {
    return this.http.get<DisplayItem[]>(this.apiEndpoint + `/category?country=${country}`);
   }

   public getCountries(): Observable<DisplayItem[]> {
    return this.http.get<DisplayItem[]>(this.apiEndpoint + '/country');
   }


   public getFAQs(): Observable<Faq[]> {
    return this.http.get<Faq[]>(this.apiEndpoint + '/faq');
   }

   public getEmployees(): Observable<DisplayItem[]> {
    return this.http.get<DisplayItem[]>(this.apiEndpoint + '/workers');
   }

   public getCurrentEmployee(id: number): Observable<Employee> {
    return this.http.get<Employee>(this.apiEndpoint + `/workers/${id}`);
   }
}
