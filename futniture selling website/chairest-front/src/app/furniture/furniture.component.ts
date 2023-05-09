import { Component } from '@angular/core';
import { Furniture } from '../models';
import { ActivatedRoute } from '@angular/router';
import { CategoryService } from '../category.service';
import { CartServiceService } from '../cart-service.service';



@Component({
  selector: 'app-furniture',
  templateUrl: './furniture.component.html',
  styleUrls: ['./furniture.component.css']
})
export class FurnitureComponent {
  furniture!: Furniture[];
  f!: Furniture;
  successMessage: string = '';

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService,
    private cartService: CartServiceService,
  ) {}

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

  addToCart(product:Furniture) {
    this.cartService.addToCart(product);
    this.successMessage = `Product '${product.title}' added to cart!`;
  }

  ngOnInit(): void {
    // const furnitureId = +this.route.snapshot.paramMap.get('id')!;
    this.categoryService.getFurnitures().subscribe((data) => {
      this.furniture = data;
    });
  }
}
