# React Native Mobile App Setup

**Arsenal configuration for mobile app development**

---

## 🎯 What This Is

A complete Arsenal setup for mobile developers who want:
- ✅ Cross-platform mobile app patterns (iOS + Android)
- ✅ Modern React Native best practices
- ✅ Navigation and state management
- ✅ API integration and authentication
- ✅ App store deployment automation

**Perfect for:**
- React Native apps
- Expo projects
- Cross-platform mobile apps
- Mobile-first startups
- MVP development

---

## ⚡ Quick Start

### Step 1: Install Arsenals

```bash
# Install all Arsenals
curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash
```

### Step 2: Create Mobile Project

```bash
# Create with Expo (recommended)
npx create-expo-app my-mobile-app
cd my-mobile-app

# Or React Native CLI
npx react-native init MyMobileApp
cd MyMobileApp
```

### Step 3: Setup Arsenal

```bash
# Create Arsenal structure
mkdir -p .windsurf/{memories,workflows}

# Copy React Native Memory
cp ~/arsenals/windsurf-memories-arsenal/project-types/react-native-memory.md \
   .windsurf/memories/ 2>/dev/null || echo "Creating custom Memory..."

# Create custom mobile Memory
cat > .windsurf/memories/mobile-app-memory.md << 'EOF'
# React Native Mobile App Memory

## Tech Stack
- React Native with Expo
- TypeScript
- React Navigation
- React Query (data fetching)
- Zustand (state management)
- Expo Router (file-based routing)

## Project Structure
/app - Screens (Expo Router)
/components - Reusable components
/services - API calls
/store - State management
/hooks - Custom hooks
/utils - Utilities
/assets - Images, fonts

## Conventions
- Functional components only
- TypeScript strict mode
- Custom hooks for logic
- Atomic design for components
- Mobile-first responsive design
EOF

# Copy workflows
cp ~/arsenals/ai-workflows-arsenal/windsurf/development/*.md \
   .windsurf/workflows/
```

### Step 4: Start Development

```bash
# Start Expo
npm start

# Open in Windsurf
windsurf .

# Ask Cascade:
"Set up the mobile app with:
- Navigation structure
- Authentication flow
- API integration
- State management
- Common screens (Home, Profile, Settings)"
```

**Result:** Mobile app foundation ready! 📱

---

## 📁 Mobile Project Structure

```
my-mobile-app/
├── .windsurf/
│   ├── memories/
│   │   ├── mobile-app-memory.md        # App context
│   │   ├── navigation-patterns.md      # Navigation
│   │   └── mobile-ui-patterns.md       # UI patterns
│   │
│   └── workflows/
│       ├── run-tests-and-fix.md        # Testing
│       ├── code-review-assistant.md    # Review
│       └── build-and-deploy.md         # Deployment
│
├── app/                                 # Screens (Expo Router)
│   ├── (auth)/
│   │   ├── login.tsx
│   │   └── signup.tsx
│   ├── (tabs)/
│   │   ├── _layout.tsx
│   │   ├── home.tsx
│   │   ├── profile.tsx
│   │   └── settings.tsx
│   └── _layout.tsx
│
├── components/
│   ├── ui/                              # Base UI components
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   └── Loading.tsx
│   ├── forms/                           # Form components
│   │   ├── LoginForm.tsx
│   │   └── ProfileForm.tsx
│   └── layouts/                         # Layout components
│       ├── Screen.tsx
│       └── Container.tsx
│
├── services/
│   ├── api.ts                          # API client
│   ├── auth.ts                         # Auth service
│   └── storage.ts                      # Local storage
│
├── store/
│   ├── useAuth.ts                      # Auth state
│   └── useUser.ts                      # User state
│
├── hooks/
│   ├── useApi.ts                       # API hook
│   ├── useAuth.ts                      # Auth hook
│   └── useTheme.ts                     # Theme hook
│
├── utils/
│   ├── validation.ts                   # Form validation
│   └── helpers.ts                      # Helper functions
│
├── assets/
│   ├── images/
│   └── fonts/
│
├── app.json                            # Expo config
├── package.json
└── tsconfig.json
```

---

## 💭 Mobile App Memory

`.windsurf/memories/mobile-app-memory.md`:

```markdown
# Mobile App Development Patterns

## Navigation Structure

### Using Expo Router (File-based)

**Layout:**
- `app/_layout.tsx` - Root layout
- `app/(tabs)/_layout.tsx` - Tab navigation
- `app/(auth)/login.tsx` - Auth screens
- `app/modal.tsx` - Modals

**Navigation:**
\`\`\`typescript
import { useRouter } from 'expo-router';

function MyComponent() {
  const router = useRouter();
  
  // Navigate
  router.push('/profile');
  
  // Go back
  router.back();
}
\`\`\`

## Component Patterns

### Screen Component
\`\`\`typescript
import { View, Text, StyleSheet } from 'react-native';
import { Screen } from '@/components/layouts/Screen';

export default function HomeScreen() {
  return (
    <Screen>
      <Text style={styles.title}>Welcome</Text>
    </Screen>
  );
}

const styles = StyleSheet.create({
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});
\`\`\`

### Reusable Button
\`\`\`typescript
import { Pressable, Text, StyleSheet } from 'react-native';

interface ButtonProps {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export function Button({ 
  title, 
  onPress, 
  variant = 'primary',
  disabled 
}: ButtonProps) {
  return (
    <Pressable
      style={[
        styles.button,
        styles[variant],
        disabled && styles.disabled
      ]}
      onPress={onPress}
      disabled={disabled}
    >
      <Text style={styles.text}>{title}</Text>
    </Pressable>
  );
}
\`\`\`

## State Management (Zustand)

\`\`\`typescript
import { create } from 'zustand';

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

export const useAuth = create<AuthState>((set) => ({
  user: null,
  token: null,
  isAuthenticated: false,
  
  login: async (email, password) => {
    const { user, token } = await authService.login(email, password);
    set({ user, token, isAuthenticated: true });
  },
  
  logout: () => {
    set({ user: null, token: null, isAuthenticated: false });
  },
}));
\`\`\`

## API Integration

\`\`\`typescript
import { useQuery, useMutation } from '@tanstack/react-query';

// Fetch data
function useUser(userId: string) {
  return useQuery({
    queryKey: ['user', userId],
    queryFn: () => api.getUser(userId),
  });
}

// Mutate data
function useUpdateProfile() {
  return useMutation({
    mutationFn: (data) => api.updateProfile(data),
    onSuccess: () => {
      queryClient.invalidateQueries(['user']);
    },
  });
}
\`\`\`

## Form Handling

\`\`\`typescript
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});

function LoginForm() {
  const { control, handleSubmit } = useForm({
    resolver: zodResolver(loginSchema),
  });
  
  const onSubmit = async (data) => {
    await authService.login(data);
  };
  
  return (
    <Controller
      control={control}
      name="email"
      render={({ field }) => (
        <Input
          {...field}
          placeholder="Email"
          keyboardType="email-address"
        />
      )}
    />
  );
}
\`\`\`

## Styling Conventions

### Use StyleSheet
- Always use StyleSheet.create()
- No inline styles (except dynamic values)
- Responsive with Dimensions API

### Theme System
\`\`\`typescript
export const theme = {
  colors: {
    primary: '#007AFF',
    secondary: '#5856D6',
    background: '#FFFFFF',
    text: '#000000',
  },
  spacing: {
    xs: 4,
    sm: 8,
    md: 16,
    lg: 24,
    xl: 32,
  },
};
\`\`\`

## Performance

### Image Optimization
- Use Expo Image component
- Optimize images before bundling
- Lazy load images

### List Performance
- Use FlashList instead of FlatList
- Implement pagination
- Memoize list items

### Bundle Size
- Code splitting with dynamic imports
- Remove unused dependencies
- Use Expo updates for OTA

## Testing

### Component Tests
\`\`\`typescript
import { render, fireEvent } from '@testing-library/react-native';

test('button calls onPress', () => {
  const onPress = jest.fn();
  const { getByText } = render(<Button title="Click" onPress={onPress} />);
  
  fireEvent.press(getByText('Click'));
  expect(onPress).toHaveBeenCalled();
});
\`\`\`

### E2E Tests
- Use Detox for E2E
- Test critical user journeys
- Run on real devices

## Deployment

### iOS (App Store)
1. Build with EAS: `eas build --platform ios`
2. Submit: `eas submit --platform ios`
3. Wait for review

### Android (Play Store)
1. Build with EAS: `eas build --platform android`
2. Submit: `eas submit --platform android`
3. Staged rollout recommended
```

---

## 🚀 Mobile Development Workflow

### Building a Feature

**Step 1: Ask Cascade**
```
"Create a user profile screen with:
- Profile photo (editable)
- User info display
- Edit profile button
- Logout button
- Settings navigation
- Loading and error states
- Pull to refresh"
```

**Step 2: Cascade Generates**
Using the Mobile Memory context:
- Screen component (`app/(tabs)/profile.tsx`)
- Profile form component
- Profile service
- Profile state (Zustand)
- Tests
- Navigation integration

**Step 3: Test**
```bash
# Run on simulator
npm run ios
# or
npm run android

# Run tests
/run-tests-and-fix
```

**Step 4: Review & Deploy**
```bash
/code-review-assistant
/commit-and-pr

# After merge, deploy
eas update --branch production
```

---

## 💡 Example Conversations

### Example 1: Authentication Flow

**You:**
```
"Implement authentication with:
- Login screen with email/password
- Signup screen
- Password validation
- JWT token storage
- Protected routes
- Auto-login on app start
- Logout functionality"
```

**Cascade (with Mobile Memory):**
- Creates login/signup screens
- Implements Zustand auth store
- Adds secure token storage
- Sets up protected route layout
- Adds form validation
- Implements auto-login
- Creates logout function
- Adds loading states

**Result:** Complete auth flow ready!

### Example 2: Product List

**You:**
```
"Create a product listing screen with:
- Grid layout (2 columns)
- Product cards with image, name, price
- Search bar
- Filter by category
- Pull to refresh
- Infinite scroll
- Loading skeleton
- Empty state"
```

**Cascade:**
- Product list screen
- Product card component
- Search component
- Filter component
- API integration with React Query
- Infinite scroll with pagination
- Loading and empty states
- Responsive grid layout

**Result:** Professional product listing!

### Example 3: Push Notifications

**You:**
```
"Add push notifications with:
- Setup Expo notifications
- Request permissions
- Handle incoming notifications
- Navigate on notification tap
- Badge count
- In-app notification display"
```

**Cascade:**
- Notification service setup
- Permission handling
- Notification listeners
- Navigation integration
- Badge management
- UI components
- Testing utilities

**Result:** Full notification system!

---

## 📱 Mobile-Specific Patterns

### Responsive Design

```typescript
import { Dimensions, Platform } from 'react-native';

const { width, height } = Dimensions.get('window');

const styles = StyleSheet.create({
  container: {
    padding: width < 375 ? 12 : 16,
  },
  title: {
    fontSize: Platform.select({
      ios: 17,
      android: 16,
    }),
  },
});
```

### Platform-Specific Code

```typescript
import { Platform } from 'react-native';

if (Platform.OS === 'ios') {
  // iOS specific
} else {
  // Android specific
}

// Or
const Component = Platform.select({
  ios: () => require('./ComponentIOS'),
  android: () => require('./ComponentAndroid'),
})();
```

### Safe Area Handling

```typescript
import { SafeAreaView } from 'react-native-safe-area-context';

export function Screen({ children }) {
  return (
    <SafeAreaView style={styles.container} edges={['top', 'bottom']}>
      {children}
    </SafeAreaView>
  );
}
```

### Keyboard Handling

```typescript
import { KeyboardAvoidingView, Platform } from 'react-native';

<KeyboardAvoidingView
  behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
  style={styles.container}
>
  {/* Form content */}
</KeyboardAvoidingView>
```

---

## 🔧 Mobile-Specific Workflows

### Build for App Stores

```bash
# iOS build
eas build --platform ios --profile production

# Android build
eas build --platform android --profile production

# Both
eas build --platform all --profile production
```

### Over-The-Air Updates

```bash
# Publish update
eas update --branch production --message "Bug fixes"

# Rollback if needed
eas update:rollback
```

### Testing on Devices

```bash
# iOS simulator
npm run ios

# Android emulator
npm run android

# Physical device
expo start
# Scan QR code with Expo Go app
```

---

## 🎨 UI/UX Best Practices

### Design System

```typescript
// theme.ts
export const theme = {
  colors: {
    primary: '#007AFF',
    secondary: '#5856D6',
    success: '#34C759',
    warning: '#FF9500',
    error: '#FF3B30',
    background: '#FFFFFF',
    surface: '#F2F2F7',
    text: {
      primary: '#000000',
      secondary: '#8E8E93',
      disabled: '#C7C7CC',
    },
  },
  typography: {
    h1: { fontSize: 34, fontWeight: 'bold' },
    h2: { fontSize: 28, fontWeight: 'bold' },
    body: { fontSize: 17, fontWeight: 'normal' },
    caption: { fontSize: 12, fontWeight: 'normal' },
  },
  spacing: {
    xs: 4,
    sm: 8,
    md: 16,
    lg: 24,
    xl: 32,
    xxl: 48,
  },
  borderRadius: {
    sm: 4,
    md: 8,
    lg: 12,
    xl: 16,
  },
};
```

### Haptics

```typescript
import * as Haptics from 'expo-haptics';

function handlePress() {
  Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
  onPress();
}
```

### Animations

```typescript
import Animated, { 
  useSharedValue, 
  useAnimatedStyle,
  withSpring 
} from 'react-native-reanimated';

function AnimatedButton() {
  const scale = useSharedValue(1);
  
  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
  }));
  
  return (
    <Animated.View style={animatedStyle}>
      {/* Button content */}
    </Animated.View>
  );
}
```

---

## 📊 Performance Optimization

### List Optimization

```typescript
import { FlashList } from '@shopify/flash-list';

<FlashList
  data={items}
  renderItem={({ item }) => <ItemCard item={item} />}
  estimatedItemSize={100}
  keyExtractor={(item) => item.id}
/>
```

### Image Optimization

```typescript
import { Image } from 'expo-image';

<Image
  source={{ uri: imageUrl }}
  placeholder={blurhash}
  contentFit="cover"
  transition={200}
  cachePolicy="memory-disk"
/>
```

### Memoization

```typescript
import { memo, useMemo, useCallback } from 'react';

const ProductCard = memo(({ product, onPress }) => {
  return (
    <Pressable onPress={() => onPress(product.id)}>
      <Text>{product.name}</Text>
    </Pressable>
  );
});

// In parent
const handlePress = useCallback((id) => {
  navigation.navigate('Product', { id });
}, [navigation]);
```

---

## 🔒 Security Best Practices

### Secure Storage

```typescript
import * as SecureStore from 'expo-secure-store';

// Save token
await SecureStore.setItemAsync('token', token);

// Get token
const token = await SecureStore.getItemAsync('token');

// Delete token
await SecureStore.deleteItemAsync('token');
```

### API Security

```typescript
// Add auth header to all requests
const api = axios.create({
  baseURL: API_URL,
  timeout: 10000,
});

api.interceptors.request.use(async (config) => {
  const token = await SecureStore.getItemAsync('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

---

## 📈 Analytics & Monitoring

### Crash Reporting

```typescript
import * as Sentry from '@sentry/react-native';

Sentry.init({
  dsn: SENTRY_DSN,
  enableAutoSessionTracking: true,
  tracesSampleRate: 1.0,
});
```

### Analytics

```typescript
import * as Analytics from 'expo-firebase-analytics';

// Track screen
await Analytics.logScreenView({
  screen_name: 'Home',
  screen_class: 'HomeScreen',
});

// Track event
await Analytics.logEvent('button_press', {
  button_name: 'login',
});
```

---

## 🎉 Success Metrics

### Before Arsenal

- ❌ Inconsistent mobile patterns
- ❌ Platform-specific bugs
- ❌ Slow feature development
- ❌ Poor performance
- ❌ Deployment complexity

### After Arsenal

- ✅ Consistent React Native patterns
- ✅ Cross-platform compatibility
- ✅ 3x faster development
- ✅ Optimized performance
- ✅ Automated deployments

---

**Mobile Arsenal = Beautiful, Fast, Cross-Platform Apps!** 📱🚀
