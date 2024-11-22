import { Component, OnInit } from '@angular/core';
import { DatosService } from '../../servicios/datos.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-lista',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lista.component.html',
  styleUrls: ['./lista.component.css']
})
export class ListaComponent implements OnInit {
  elementos: any[] = []; // Datos del backend

  constructor(private datosService: DatosService) {}

  ngOnInit(): void { 
    this.datosService.obtenerDatos().subscribe(
      (data) => {
        this.elementos = data;
      },
      (error) => {
        console.error('Error al obtener los elementos:', error);
      }
    );
  }
}
