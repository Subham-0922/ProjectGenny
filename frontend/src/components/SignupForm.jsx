import React, { useState } from "react";

const SignupForm = () => {
  const [showLoginForm, setShowLoginForm] = useState(true);
  const [role, setRole] = useState("");
  const [showSecretKey, setShowSecretKey] = useState(false);

  const handleFormToggle = () => {
    setShowLoginForm((prevState) => !prevState);
  };

  const handleRoleChange = (event) => {
    const selectedRole = event.target.value;
    setRole(selectedRole);
    setShowSecretKey(selectedRole === "ADMIN");
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Perform form submission and other actions here
    // Access form values using event.target elements or React refs
  };

  return (
    <div className="container">
      {showLoginForm ? (
        <form onSubmit={handleSubmit}>
          <h2>Login</h2>
          <div class="form-group">
            <label for="login-email">Email</label>
            <input type="email" id="login-email" name="login-email" required />
          </div>
          <div class="form-group">
            <label for="login-password">Password</label>
            <input
              type="password"
              id="login-password"
              name="login-password"
              required
            />
          </div>
          
          <div className="form-group">
            <button type="submit">Login</button>
          </div>
          <div className="switch-form">
            <p>
              New user?{" "}
              <button type="button" onClick={handleFormToggle}>
                Sign Up
              </button>
            </p>
          </div>
        </form>
      ) : (
        <form onSubmit={handleSubmit}>
          <h2>Sign Up</h2>
          <div className="form-group">
            <label htmlFor="signup-name">Name</label>
            <input type="text" id="signup-name" name="signup-name" required />
          </div>
          
          <div className="form-group">
            <label htmlFor="signup-email">Email</label>
            <input
              type="email"
              id="signup-email"
              name="signup-email"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="signup-password">Password</label>
            <input
              type="password"
              id="signup-password"
              name="signup-password"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="signup-role">Role</label>
            <select
              id="signup-role"
              name="signup-role"
              value={role}
              onChange={handleRoleChange}
              required
            >
              <option value="" disabled>
                Select Role
              </option>
              <option value="ADMIN">ADMIN</option>
              <option value="Manager">Manager</option>
            </select>
          </div>
          {showSecretKey && (
            <div className="form-group">
              <label htmlFor="signup-secret-key">Secret Key</label>
              <input
                type="password"
                id="signup-secret-key"
                name="signup-secret-key"
              />
            </div>
          )}
          <div className="form-group">
            <label htmlFor="signup-bio">Bio</label>
            <textarea id="signup-bio" name="signup-bio" rows="4"></textarea>
          </div>
          <div className="form-group">
            <button type="submit">Sign Up</button>
          </div>
          <div className="switch-form">
            <p>
              Already have an account?{" "}
              <button type="button" onClick={handleFormToggle}>
                Login
              </button>
            </p>
          </div>
        </form>
      )}
    </div>
  );
};

export default SignupForm;
