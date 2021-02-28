import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Hero } from './hero';

@Injectable({
  providedIn: 'root'
})
export class HeroService {

  private heroesUrl = 'http://127.0.0.1:8000/heroes'

  httpOptions = {
    headers: new HttpHeaders({'Content-Type': 'application/json' })
  }

  constructor(private http: HttpClient) { }

  getHeroes(): Observable<any>{
    return this.http.get<any>(this.heroesUrl);
  }

  getHero(id: any): Observable<any>{
    return this.http.get<any>(`${this.heroesUrl}/${id}`);
  }

  addHero(hero: Hero): Observable<any>{
    return this.http.post(this.heroesUrl, hero, this.httpOptions)
  }

  updateHero(hero: Hero): Observable<any>{
    return this.http.put(this.heroesUrl, hero, this.httpOptions);
  }

 deleteHero(id: any): Observable<any>{
   return this.http.delete(`${this.heroesUrl}/${id}`) 
 }
}
