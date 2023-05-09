import {Component, OnInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CategoryService } from '../category.service';

@Component({
  selector: 'app-category-detail',
  templateUrl: './category-detail.component.html',
  styleUrls: ['./category-detail.component.css']
})
export class CategoryDetailComponent implements OnInit {
  categoryId?: number;
  category: any;
  furniture?: any[];

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService
  ) { }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.categoryId = Number(params.get('id'));
      this.categoryService.getCategory(this.categoryId).subscribe(category => {
        this.category = category;
      });
      this.categoryService.getFurniture(this.categoryId).subscribe(furniture => {
        this.furniture = furniture;
      });
    });
  }
}
