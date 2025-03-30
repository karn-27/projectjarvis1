import React from "react";

export const Input = ({ type, placeholder, className, ...props }) => {
  return (
    <input
      type={type}
      placeholder={placeholder}
      className={`px-3 py-2 border rounded ${className}`}
      {...props}
    />
  );
};
