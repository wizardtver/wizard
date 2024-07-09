import { User } from "../user/User";
import { Product } from "../product/Product";

export type Review = {
  id: string;
  createdAt: Date;
  updatedAt: Date;
  rating: number | null;
  reviewText: string | null;
  user?: User | null;
  product?: Product | null;
};
