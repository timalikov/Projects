import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoryFurnitureListComponent } from './category-furniture-list.component';

describe('CategoryFurnitureListComponent', () => {
  let component: CategoryFurnitureListComponent;
  let fixture: ComponentFixture<CategoryFurnitureListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CategoryFurnitureListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CategoryFurnitureListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
