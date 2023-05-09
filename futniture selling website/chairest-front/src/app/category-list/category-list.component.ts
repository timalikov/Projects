import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { CategoryService } from '../category.service';
import { Category } from '../models';
@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent implements OnInit {
  categories!: Category[];

  constructor(private categoryService: CategoryService, private router: Router) { }

  ngOnInit() {
    this.categoryService.getCategories().subscribe(
        (response) => {
          this.categories = response;
        },
      );
    
  }

  gotoDetail(category: Category): void {
    const link = ['/categories', category.id];
    this.router.navigate(link);
  }
}
