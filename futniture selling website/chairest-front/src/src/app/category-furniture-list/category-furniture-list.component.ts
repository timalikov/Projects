import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {Category, Furniture} from '../models';
import { FurnitureService } from '../furniture.service';
import { CategoryService } from '../category.service';
@Component({
  selector: 'app-category-furniture-list',
  templateUrl: './category-furniture-list.component.html',
  styleUrls: ['./category-furniture-list.component.css']
})
export class CategoryFurnitureListComponent implements OnInit {
  categoryId!: number;
  furniture!: Furniture[];

  constructor(
    private route: ActivatedRoute,
    private furnitureService: FurnitureService
  ) { }

  ngOnInit(): void {
    this.categoryId = +this.route.snapshot.paramMap.get('id')!;
    this.furnitureService.getFurnitureByCategory(this.categoryId)
      .subscribe(furniture => this.furniture = furniture);
  }
}
