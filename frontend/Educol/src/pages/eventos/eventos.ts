import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';

/**
 * Generated class for the EventosPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-eventos',
  templateUrl: 'eventos.html',
})
export class EventosPage {
  eventos: any;

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: RestProvider) {
  }

  ionViewDidLoad() {
    this.consultarEventos();
    console.log('ionViewDidLoad EventosPage');
  }

  consultarEventos() {
    this.restProvider.getEventos()
    .then(data => {
    this.eventos = data;
    });
    }
   

}
