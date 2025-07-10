import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeroLike } from './hero-like';

describe('HeroLike', () => {
  let component: HeroLike;
  let fixture: ComponentFixture<HeroLike>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [HeroLike]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeroLike);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
