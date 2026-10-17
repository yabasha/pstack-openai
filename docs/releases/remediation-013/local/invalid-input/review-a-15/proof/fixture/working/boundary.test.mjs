import { test, expect } from 'bun:test';
import { orderHttp } from './adapter.ts';
import { exampleTotal } from './internal-caller.ts';
test('all external invalid quantities retain boundary error', () => {
  for (const raw of ['{}','{"quantity":null}','{"quantity":0}','{"quantity":-1}','{"quantity":1.5}','{"quantity":"2"}']) {
    expect(orderHttp(raw)).toEqual({ status: 400, body: { error: 'invalid quantity' } });
  }
});
test('existing outer guard and parser remain necessary', () => {
  for (const raw of ['null','[]','"text"']) expect(orderHttp(raw)).toEqual({ status: 400, body: { error: 'invalid order' } });
  expect(orderHttp('{')).toEqual({ status: 400, body: { error: 'invalid json' } });
});
test('valid external and typed internal consumers', () => {
  expect(orderHttp('{"quantity":2}')).toEqual({ status: 200, body: { total: 250 } });
  expect(exampleTotal()).toBe(250);
});
