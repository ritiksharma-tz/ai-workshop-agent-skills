import type { ReactNode } from 'react';

export interface ExampleProps {
  /** The main content to display */
  children: ReactNode;
  /** Visual variant */
  variant?: 'primary' | 'secondary';
  /** Optional click handler */
  onClick?: () => void;
}

export function Example({ children, variant = 'primary', onClick }: ExampleProps) {
  return (
    <div
      className={`example example--${variant}`}
      onClick={onClick}
      role={onClick ? 'button' : undefined}
    >
      {children}
    </div>
  );
}

export default Example;
