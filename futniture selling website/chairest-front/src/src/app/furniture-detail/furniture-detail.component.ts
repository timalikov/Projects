import { Component } from '@angular/core';
import {Furniture} from "../models";
import {ActivatedRoute} from "@angular/router";
import {CategoryService} from "../category.service";

@Component({
  selector: 'app-furniture-detail',
  templateUrl: './furniture-detail.component.html',
  styleUrls: ['./furniture-detail.component.css']
})
export class FurnitureDetailComponent {
  furniture?: Furniture[];

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService,
  ) {}

  ngOnInit(): void {
    const furnitureId = +this.route.snapshot.paramMap.get('id')!;
    this.categoryService.getFurniture(furnitureId).subscribe((data) => {
      this.furniture = data;
    });
  }
}
