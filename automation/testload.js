import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  http.get('http://139.144.176.188');
  sleep(1);
}
