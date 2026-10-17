import { test, expect } from 'bun:test';
import { priceOrder, subtotal } from './domain.ts';

test('subtotal prices positive quantities in integer cents', () => {
  expect(subtotal(1)).toBe(125);
  expect(subtotal(3)).toBe(375);
});

test('priceOrder prices a trusted typed order', () => {
  expect(priceOrder({ quantity: 4 })).toBe(500);
});
