
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../api/api';

const Register = () => {
  const [formData, setFormData] = useState({ full_name: '', email: '', password: '' });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    setLoading(true);
    setError('');
    try {
      await api.post('/api/v1/auth/register', formData);
      navigate('/login');
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display:'flex', justifyContent:'center', alignItems:'center', minHeight:'100vh', background:'#f5f5f5' }}>
      <div style={{ background:'white', padding:'2rem', borderRadius:'8px', boxShadow:'0 2px 10px rgba(0,0,0,0.1)', width:'100%', maxWidth:'400px' }}>
        <h2 style={{ textAlign:'center', color:'#1a2b4a' }}>Create an Account</h2>
        <p style={{ textAlign:'center', color:'#666' }}>Or <Link to="/login">sign in</Link></p>
        <div style={{ marginBottom:'1rem' }}>
          <label>Full Name</label>
          <input type="text" name="full_name" value={formData.full_name} onChange={handleChange} placeholder="Enter your full name" style={{ width:'100%', padding:'0.75rem', border:'1px solid #ddd', borderRadius:'4px', boxSizing:'border-box', marginTop:'0.25rem' }} />
        </div>
        <div style={{ marginBottom:'1rem' }}>
          <label>Email address</label>
          <input type="email" name="email" value={formData.email} onChange={handleChange} placeholder="Enter your email" style={{ width:'100%', padding:'0.75rem', border:'1px solid #ddd', borderRadius:'4px', boxSizing:'border-box', marginTop:'0.25rem' }} />
        </div>
        <div style={{ marginBottom:'1rem' }}>
          <label>Password</label>
          <input type="password" name="password" value={formData.password} onChange={handleChange} placeholder="Enter your password" style={{ width:'100%', padding:'0.75rem', border:'1px solid #ddd', borderRadius:'4px', boxSizing:'border-box', marginTop:'0.25rem' }} />
        </div>
        {error && <p style={{ color:'red', textAlign:'center' }}>{error}</p>}
        <button onClick={handleSubmit} disabled={loading} style={{ width:'100%', padding:'0.75rem', background:'#2196F3', color:'white', border:'none', borderRadius:'4px', cursor:'pointer', fontSize:'1rem' }}>
          {loading ? 'Creating account...' : 'Create Account'}
        </button>
      </div>
    </div>
  );
};

export default Register;
EOF