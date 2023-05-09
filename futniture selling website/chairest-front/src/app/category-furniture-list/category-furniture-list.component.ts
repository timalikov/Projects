import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {Category, Furniture} from '../models';
import { FurnitureService } from '../furniture.service';
import { CartServiceService } from '../cart-service.service';
import { CategoryService } from '../category.service';

@Component({
  selector: 'app-category-furniture-list',
  templateUrl: './category-furniture-list.component.html',
  styleUrls: ['./category-furniture-list.component.css']
})
export class CategoryFurnitureListComponent implements OnInit {
  categoryId!: number;
  successMessage: string = '';
  furniture!: Furniture[];

  constructor(
    private route: ActivatedRoute,
    private furnitureService: FurnitureService,
    private cartService: CartServiceService,
  ) { }

  addToCart(product:Furniture) {
    this.cartService.addToCart(product);
    this.successMessage = `Product '${product.title}' added to cart!`;
  }

  
  isExpanded(f: Furniture): boolean {
    return f.isExpanded;
  }

  toggleExpanded(f: Furniture): void {
    f.isExpanded = !this.isExpanded(f);
  }

  getDescriptionText(f: Furniture): string {
    if (this.isExpanded(f)) {
      return f.description;
    } else {
      const maxDescriptionLength = 100; // Adjust this value as needed
      if (f.description.length > maxDescriptionLength) {
        return f.description.slice(0, maxDescriptionLength) + '...';
      } else {
        return f.description;
      }
    }
  }

  shouldDisplayViewMore(f: Furniture): boolean {
    const maxDescriptionLength = 100; // Adjust this value as needed
    return !this.isExpanded(f) && f.description.length > maxDescriptionLength;
  }

  ngOnInit(): void {
    this.categoryId = +this.route.snapshot.paramMap.get('id')!;
    this.furnitureService.getFurnitureByCategory(this.categoryId)
      .subscribe(furniture => this.furniture = furniture);
  }
}
