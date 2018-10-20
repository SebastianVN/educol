import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
/*
 Generated class for the RestProvider provider.
 See https://angular.io/guide/dependency-injection for more info on providers
 and Angular DI.
*/
@Injectable()
export class RestProvider {

  apiUrl = 'http://1ce53c09.ngrok.io/';
  loginService = 'api/login/';
  apiEvento = 'evento/'
  apiUsuarios = 'usuarios/';

  constructor(public http: HttpClient) {
    console.log('Hello RestProvider Provider');
  }
  //REGISTRO y lOGIN
  login(data) {
    return new Promise((resolve, reject) => {
      this.http.post(this.apiUrl + this.loginService, data)
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }

  registro(data) {
    return new Promise((resolve, reject) => {
      this.http.post(this.apiUrl + this.apiUsuarios, data)
        .subscribe(res => {
          resolve(res);
        }, (err) => {
          reject(err);
        });
    });
  }
  //Consultas a las demas API
  getEventos() {
    return new Promise(resolve => {
      this.http.get(this.apiUrl + this.apiEvento, {
        headers: new HttpHeaders().set('Authorization', 'token ' + window.localStorage['token'])
      }).subscribe(data => {
        resolve(data);
      }, err => {
        console.log(err);
      });
    });
  }
}


