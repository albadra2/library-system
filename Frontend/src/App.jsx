import { Routes, Route, Link } from "react-router-dom";
import HomePage from './views/HomePage';
import GenresView from './views/GenresView';
import AuthorPage from './views/AuthorPage';
import BorrowingsList from './views/BorrowingsList';
import CustomerInfo from './views/CustomerInfo';

export default function App() {
  return (
    <div className="container">
      <nav>
        <Link to="/admin">Admin Login</Link>
        <Link to="/">Books</Link>
        <Link to="/authors">Authors</Link><Link to="/genres">Genres</Link>
        <Link to="/borrowings">Overdue</Link>
        <Link to="/customers">Customers</Link>
      </nav>
      <Routes>
        <Route path="/" element={<HomePage />} />\n<Route path="/authors" element={<AuthorPage />} />
        <Route path="/genres" element={<GenresView />} />
        <Route path="/borrowings" element={<BorrowingsList />} />
        <Route path="/customers" element={<CustomerInfo />} />
      </Routes>
    </div>
  );
}
