import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { Example } from './Example';

describe('Example', () => {
  it('renders children', () => {
    render(<Example>Hello World</Example>);
    expect(screen.getByText('Hello World')).toBeInTheDocument();
  });

  it('applies variant class', () => {
    const { container } = render(<Example variant="secondary">Test</Example>);
    expect(container.firstChild).toHaveClass('example--secondary');
  });

  it('handles click events', () => {
    const handleClick = vi.fn();
    render(<Example onClick={handleClick}>Click me</Example>);
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledOnce();
  });
});
