import React, { useEffect, useState } from 'react';

export default function CustomerInfo() {
  const [customers, setCustomers] = useState([]);
  const [borrowings, setBorrowings] = useState({});

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL + '/customers/')
      .then(res => res.json())
      .then(data => setCustomers(data))
      .catch(err => alert('Failed to load customers.'));
  }, []);

  useEffect(() => {
    customers.forEach(customer => {
      fetch(process.env.REACT_APP_API_URL + `/borrowings/?customer=${customer.id}`)
        .then(res => res.json())
        .then(data => {
          setBorrowings(prev => ({ ...prev, [customer.id]: data }));
        });
    });
  }, [customers]);

  return (
    <div>
      <h2>Customers and Borrowings</h2>
      {customers.map(c => (
        <div key={c.id}>
          <strong>{c.first_name} {c.last_name}</strong><br/>
          Email: {c.email}<br/>
          <em>Borrowed Books:</em><br/>
          <ul>
            {(borrowings[c.id] || []).map(b => (
              <li key={b.id}>Book ID: {b.book} | Due: {b.due_date}</li>
            ))}
          </ul>
          <br/>
        </div>
      ))}
    </div>
  );
}
