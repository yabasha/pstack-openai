import { runBatch, type Order } from "./index";

export function invoiceTotals(): Array<number | null> {
  const orders: Order[] = [
    { quantity: 2, unitPrice: 125 },
    { quantity: 1, unitPrice: 99 },
  ];
  return runBatch(orders);
}
