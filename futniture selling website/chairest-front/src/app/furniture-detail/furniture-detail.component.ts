import { Component, OnInit } from '@angular/core';
import {Furniture} from "../models";
import {ActivatedRoute} from "@angular/router";
import { CategoryService } from '../category.service';
import { FurnitureComponent } from '../furniture/furniture.component';
import { Location } from '@angular/common';


@Component({
  selector: 'app-furniture-detail',
  templateUrl: './furniture-detail.component.html',
  styleUrls: ['./furniture-detail.component.css']
})
export class FurnitureDetailComponent implements OnInit{
  furnitureId?: number;
  category: any;
  furniture!: Furniture;

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService,
    private location: Location
  ) { }

  goBackToPreviousAPI() {
    this.location.back();
  }
  
  

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.furnitureId = Number(params.get('id'));
      this.categoryService.getFurniture(this.furnitureId).subscribe((data) => {
        this.furniture = data;
      });
    });
  }

  // furnitureId?: number;
  // furniture!: Furniture;
  // pricing?: any[];

  // constructor(
  //   private route: ActivatedRoute,
  //   private categoryService: CategoryService,
  // ) { }

  // ngOnInit() {
  //   this.route.paramMap.subscribe(params => {
  //     this.furnitureId = Number(params.get('id'));
  //     this.categoryService.getFurniture(this.furnitureId).subscribe((data) => {
  //       this.furniture = data;
  //     });
  //   });
  // }
}


  // furniture!: Furniture;
  // furnitureId: number;

  // constructor(
  //   private route: ActivatedRoute,
  //   private categoryService: CategoryService,
    // private http: HttpClient
  // ) {}

  // ngOnInit(): void {
  //   this.furnitureId = this.route.snapshot.paramMap.get('id');
  //   // this.fetchFurnitureData(this.furnitureId);
  //   // const furnitureId = +this.route.snapshot.paramMap.get('id')!;
  //   this.categoryService.getFurniture(this.furnitureId).subscribe((data) => {
  //     this.furniture = data;
  //   });
  //

