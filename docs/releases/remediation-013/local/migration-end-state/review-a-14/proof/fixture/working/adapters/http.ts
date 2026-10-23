import { total, type Order } from '../domain/order';

function isHttpOrder(value: unknown): value is Order {
  return typeof value === 'object' && value !== null
    && 'quantity' in value && typeof value.quantity === 'number'
    && Number.isInteger(value.quantity) && value.quantity > 0
    && 'unitPrice' in value && typeof value.unitPrice === 'number'
    && Number.isInteger(value.unitPrice) && value.unitPrice >= 0;
}

export function handle(raw: string): { status: number; body: string } {
  let order: unknown;
  try {
    order = JSON.parse(raw);
  } catch {
    return { status: 400, body: 'invalid json' };
  }
  if (!isHttpOrder(order)) return { status: 400, body: 'invalid order' };
  return { status: 200, body: JSON.stringify({ total: total(order) }) };
}
