import { priceOrder, type Order } from './domain';

export function orderHttp(raw: string): { status: number; body: { total?: number; error?: string } } {
  let value: unknown;
  try { value = JSON.parse(raw); } catch { return { status: 400, body: { error: 'invalid json' } }; }
  if (typeof value !== 'object' || value === null || Array.isArray(value)) return { status: 400, body: { error: 'invalid order' } };

  const quantity = 'quantity' in value ? value.quantity : undefined;
  if (typeof quantity !== 'number' || !Number.isInteger(quantity) || quantity <= 0) return { status: 400, body: { error: 'invalid quantity' } };

  const order: Order = { quantity };
  return { status: 200, body: { total: priceOrder(order) } };
}
