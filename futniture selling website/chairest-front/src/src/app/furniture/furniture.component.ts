import { Component, Input } from '@angular/core';
import { Furniture } from '../models';
import { ActivatedRoute } from '@angular/router';
import { CategoryService } from '../category.service';
@Component({
  selector: 'app-furniture',
  templateUrl: './furniture.component.html',
  styleUrls: ['./furniture.component.css']
})
export class FurnitureComponent {
  furniture!: Furniture[];

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService,
  ) {}

  ngOnInit(): void {
    // const furnitureId = +this.route.snapshot.paramMap.get('id')!;
    this.categoryService.getFurnitures().subscribe((data) => {
      this.furniture = data;
    });
  }
}
